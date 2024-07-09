-- Create a tables  for the project
CREATE DATABASE IF NOT EXISTS pharmap_db;
CREATE USER IF NOT EXISTS "pharmap_dev"@"localhost" IDENTIFIED BY "pharmapwd";
GRANT ALL PRIVILEGES ON pharmap_db.* TO "pharmap_dev"@"localhost";
GRANT SELECT ON performance_schema.* TO "pharmap_dev"@"localhost";

-- create a testing database and user
CREATE DATABASE IF NOT EXISTS pharma_test_db;
CREATE USER IF NOT EXISTS "pharmap_test"@"localhost" IDENTIFIED BY "pharmaptestpwd";
GRANT ALL PRIVILEGES ON pharma_test_db.*  TO "pharmap_test"@"localhost";
GRANT SELECT ON performance_schema.* TO "pharmap_test"@"localhost";
