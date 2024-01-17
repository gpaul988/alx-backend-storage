-- Generate indication idx_name_first on the table names and the first letter of name.
-- Graham S. Paul - 8-index_my_names.sql
CREATE INDEX idx_name_first ON names(name(1));
