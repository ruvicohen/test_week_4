--query 1

SELECT air_force, COUNT(*) AS mission_count
FROM mission
WHERE EXTRACT(YEAR FROM mission_date) = 1943
GROUP BY air_force
ORDER BY mission_count DESC
LIMIT 1;

--b-tree index
CREATE INDEX idx_mission_date ON mission (extract (YEAR FROM mission_date))
--hash index
CREATE INDEX idx_mission_date ON mission using hash (extract (YEAR FROM mission_date))


--query 2
select bomb_damage_assessment, count(target_country) from mission
where bomb_damage_assessment is not null
and airborne_aircraft > 5
group by target_country, bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1

--b-tree index
CREATE INDEX idx_bomb_damage_assessment ON mission (bomb_damage_assessment)
--hash index
CREATE INDEX idx_bomb_damage_assessment ON mission using hash (bomb_damage_assessment)




