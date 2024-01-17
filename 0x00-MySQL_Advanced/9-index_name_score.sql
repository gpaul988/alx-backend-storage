-- Generates indication for  idx_name_first_score on the table names
-- Graham S. Paul - 9-index_name_score.sql
CREATE INDEX idx_name_first_score ON names(name(1), score);
