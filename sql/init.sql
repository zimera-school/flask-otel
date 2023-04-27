--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_table_access_method = heap;

CREATE TABLE public.organization (
    organization_id integer NOT NULL,
    name character varying(100) NOT NULL,
    tagline character varying(250),
    website character varying(100),
    email character varying(30)
);


ALTER TABLE public.organization OWNER TO postgres;

CREATE SEQUENCE public.organization_organization_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.organization_organization_id_seq OWNER TO postgres;

ALTER SEQUENCE public.organization_organization_id_seq OWNED BY public.organization.organization_id;

ALTER TABLE ONLY public.organization ALTER COLUMN organization_id SET DEFAULT nextval('public.organization_organization_id_seq'::regclass);


COPY public.organization (organization_id, name, tagline, website, email) FROM stdin;
1	The Corporation	Here is our tagline	https://web.com	info@web.com
2	The Second Corporation	The second tagline	http://web2.com	info@web2.com
\.

SELECT pg_catalog.setval('public.organization_organization_id_seq', 2, true);


ALTER TABLE ONLY public.organization
    ADD CONSTRAINT organization_pkey PRIMARY KEY (organization_id);

--
-- PostgreSQL database dump complete
--

