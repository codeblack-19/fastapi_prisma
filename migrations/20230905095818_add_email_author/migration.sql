-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_Author" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "email" TEXT NOT NULL DEFAULT 'test@testing.com'
);
INSERT INTO "new_Author" ("id", "name") SELECT "id", "name" FROM "Author";
DROP TABLE "Author";
ALTER TABLE "new_Author" RENAME TO "Author";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
