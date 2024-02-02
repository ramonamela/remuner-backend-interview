-- upgrade --
CREATE UNIQUE INDEX "uid_integration_name_674a6d" ON "integrations" ("name");
-- downgrade --
DROP INDEX "idx_integration_name_674a6d";
