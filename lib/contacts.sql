BEGIN;

    SET client_encoding
    = 'LATIN1';

CREATE TABLE contacts
(
    id integer NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    area_code integer NOT NULL,
    phone_number integer NOT NULL
);

-- Data for Contacts 
COPY contacts
(id, first_name, last_name, area_code, phone_number) FROM stdin;
1	Scott   Kutler  469 3870895
2	Noah    Clark   202 5552020	
3	Roger   Campbell    202 5551010
\.


ALTER TABLE ONLY contacts
ADD CONSTRAINT contacts_pkey PRIMARY KEY
(id);

COMMIT;

-- ANALYZE contacts