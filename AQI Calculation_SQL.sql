SELECT 
    *,
    -- Data Quality Check
    CASE WHEN pm10 IS NOT NULL AND pm10 > 0 THEN 1 ELSE 0 END as PM10_Quality,
    CASE WHEN pm2_5 IS NOT NULL AND pm2_5 > 0 THEN 1 ELSE 0 END as PM2_5_Quality,
    CASE WHEN co IS NOT NULL AND co > 0 THEN 1 ELSE 0 END as CO_Quality,
    CASE WHEN no IS NOT NULL AND no > 0 THEN 1 ELSE 0 END as NO2_Quality,
    CASE WHEN ozone IS NOT NULL AND ozone > 0 THEN 1 ELSE 0 END as Ozone_Quality,
    CASE WHEN so2 IS NOT NULL AND so2 > 0 THEN 1 ELSE 0 END as SO2_Quality,

    -- AQI Calculation
    CASE 
        WHEN 
            (CASE WHEN pm10 IS NOT NULL AND pm10 > 0 THEN 1 ELSE 0 END +
             CASE WHEN pm2_5 IS NOT NULL AND pm2_5 > 0 THEN 1 ELSE 0 END +
             CASE WHEN co IS NOT NULL AND co > 0 THEN 1 ELSE 0 END +
             CASE WHEN no IS NOT NULL AND no > 0 THEN 1 ELSE 0 END +
             CASE WHEN ozone IS NOT NULL AND ozone > 0 THEN 1 ELSE 0 END +
             CASE WHEN so2 IS NOT NULL AND so2 > 0 THEN 1 ELSE 0 END) >= 3 AND 
            (pm10 IS NOT NULL OR pm2_5 IS NOT NULL)
        THEN 
            GREATEST(
                COALESCE(PM10_Sub_Index, 0), 
                COALESCE(PM2_5_Sub_Index, 0), 
                COALESCE(CO_Sub_Index, 0), 
                COALESCE(NO2_Sub_Index, 0), 
                COALESCE(Ozone_Sub_Index, 0), 
                COALESCE(SO2_Sub_Index, 0)
            )
        ELSE NULL 
    END as AQI
FROM (
    SELECT *,
        -- PM10 Sub-Index
        CASE 
            WHEN COALESCE(pm10,0) BETWEEN 0 AND 50 THEN pm10
            WHEN COALESCE(pm10,0) BETWEEN 51 AND 100 THEN pm10
            WHEN COALESCE(pm10,0) BETWEEN 101 AND 250 THEN 100 + (pm10 - 100) * 100 / 150
            WHEN COALESCE(pm10,0) BETWEEN 251 AND 350 THEN 200 + (pm10 - 250)
            WHEN COALESCE(pm10,0) BETWEEN 351 AND 430 THEN 300 + (pm10 - 350) * 100 / 80
            WHEN COALESCE(pm10,0) > 430 THEN 400 + (pm10 - 430) * 100 / 80
            ELSE 0
        END as PM10_Sub_Index,

        -- PM2.5 Sub-Index
        CASE 
            WHEN COALESCE(pm2_5,0) BETWEEN 0 AND 30 THEN pm2_5 * 50 / 30
            WHEN COALESCE(pm2_5,0) BETWEEN 31 AND 60 THEN 50 + (pm2_5 - 30) * 50 / 30
            WHEN COALESCE(pm2_5,0) BETWEEN 61 AND 90 THEN 100 + (pm2_5 - 60) * 100 / 30
            WHEN COALESCE(pm2_5,0) BETWEEN 91 AND 120 THEN 200 + (pm2_5 - 90) * 100 / 30
            WHEN COALESCE(pm2_5,0) BETWEEN 121 AND 250 THEN 300 + (pm2_5 - 120) * 100 / 130
            WHEN COALESCE(pm2_5,0) > 250 THEN 400 + (pm2_5 - 250) * 100 / 130
            ELSE 0
        END as PM2_5_Sub_Index,

        -- CO Sub-Index
        CASE 
            WHEN COALESCE(co,0) BETWEEN 0 AND 1 THEN co * 50 / 1
            WHEN COALESCE(co,0) BETWEEN 1.1 AND 2 THEN 50 + (co - 1) * 50 / 1
            WHEN COALESCE(co,0) BETWEEN 2.1 AND 10 THEN 100 + (co - 2) * 100 / 8
            WHEN COALESCE(co,0) BETWEEN 10.1 AND 17 THEN 200 + (co - 10) * 100 / 7
            WHEN COALESCE(co,0) BETWEEN 17.1 AND 34 THEN 300 + (co - 17) * 100 / 17
            WHEN COALESCE(co,0) > 34 THEN 400 + (co - 34) * 100 / 17
            ELSE 0
        END as CO_Sub_Index,

        -- NO2 Sub-Index
        CASE 
            WHEN COALESCE(no,0) BETWEEN 0 AND 40 THEN no * 50 / 40
            WHEN COALESCE(no,0) BETWEEN 41 AND 80 THEN 50 + (no - 40) * 50 / 40
            WHEN COALESCE(no,0) BETWEEN 81 AND 180 THEN 100 + (no - 80) * 100 / 100
            WHEN COALESCE(no,0) BETWEEN 181 AND 280 THEN 200 + (no - 180) * 100 / 100
            WHEN COALESCE(no,0) BETWEEN 281 AND 400 THEN 300 + (no - 280) * 100 / 120
            WHEN COALESCE(no,0) > 400 THEN 400 + (no - 400) * 100 / 120
            ELSE 0
        END as NO2_Sub_Index,

        -- Ozone Sub-Index
        CASE 
            WHEN COALESCE(ozone,0) BETWEEN 0 AND 50 THEN ozone
            WHEN COALESCE(ozone,0) BETWEEN 51 AND 100 THEN 50 + (ozone - 50) * 50 / 50
            WHEN COALESCE(ozone,0) BETWEEN 101 AND 168 THEN 100 + (ozone - 100) * 100 / 68
            WHEN COALESCE(ozone,0) BETWEEN 169 AND 208 THEN 200 + (ozone - 168) * 100 / 40
            WHEN COALESCE(ozone,0) BETWEEN 209 AND 748 THEN 300 + (ozone - 208) * 100 / 539
            WHEN COALESCE(ozone,0) > 748 THEN 400 + (ozone - 748) * 100 / 539
            ELSE 0
        END as Ozone_Sub_Index,

        -- SO2 Sub-Index
        CASE 
            WHEN COALESCE(so2,0) BETWEEN 0 AND 40 THEN so2 * 50 / 40
            WHEN COALESCE(so2,0) BETWEEN 41 AND 80 THEN 50 + (so2 - 40) * 50 / 40
            WHEN COALESCE(so2,0) BETWEEN 81 AND 380 THEN 100 + (so2 - 80) * 100 / 300
            WHEN COALESCE(so2,0) BETWEEN 381 AND 800 THEN 200 + (so2 - 380) * 100 / 420
            WHEN COALESCE(so2,0) BETWEEN 801 AND 1600 THEN 300 + (so2 - 800) * 100 / 800
            WHEN COALESCE(so2,0) > 1600 THEN 400 + (so2 - 1600) * 100 / 800
            ELSE 0
        END as SO2_Sub_Index
    FROM cowi.cowi_aqi_data
) as sub_indices
