CREATE INDEX "student_id_index" ON "enrollments" ("student_id");

CREATE INDEX "department_index" ON "courses" ("department");

CREATE INDEX "course_id_index" ON "enrollments" ("course_id");

CREATE INDEX "semester_index" ON "courses" ("semester");

CREATE INDEX "course_id_satisfies_index" ON "satisfies" ("course_id");
