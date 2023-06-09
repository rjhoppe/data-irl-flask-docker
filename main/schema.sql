DROP TABLE IF EXISTS requests;

CREATE TABLE requests (
    requestid INTEGER PRIMARY KEY AUTOINCREMENT,
    submit_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    submit_date TEXT NOT NULL DEFAULT CURRENT_DATE,
    email TEXT NOT NULL,
    surveyurl TEXT NOT NULL,
    respGen TEXT NOT NULL,
    responseType TEXT NOT NULL
);