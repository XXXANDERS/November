CREATE TABLE IF NOT EXISTS users (
                            ID SERIAL PRIMARY KEY,
                            USERNAME VARCHAR(50) NOT NULL,
                            PHONE VARCHAR(20),
                            NAME VARCHAR(25)
                            );
