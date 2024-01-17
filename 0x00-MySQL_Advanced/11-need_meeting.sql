-- Generate an insight need_meeting that lists all students that have a score
-- below 80 (strict) and no last_meeting or more than 1 month.
-- Graham S. Paul - 11-need_meeting.sql
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
    SELECT name
        FROM students
        WHERE score < 80 AND
            (
                last_meeting IS NULL
                OR last_meeting < SUBDATE(CURRENT_DATE(), INTERVAL 1 MONTH)
            )
;
