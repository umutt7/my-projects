-- The most proficient districts in order
SELECT "districts"."name", "staff_evaluations"."proficient" FROM "districts"
JOIN "staff_evaluations" ON "staff_evaluations"."district_id" = "districts"."id"
ORDER BY "proficient" DESC;
