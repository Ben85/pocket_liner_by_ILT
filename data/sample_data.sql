--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: marci
--

CREATE TABLE categories (
    id integer NOT NULL,
    category character varying(255) NOT NULL,
    transaction_type integer NOT NULL
);


ALTER TABLE categories OWNER TO marci;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: marci
--

CREATE SEQUENCE categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE categories_id_seq OWNER TO marci;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: marci
--

ALTER SEQUENCE categories_id_seq OWNED BY categories.id;


--
-- Name: transactions; Type: TABLE; Schema: public; Owner: marci
--

CREATE TABLE transactions (
    id integer NOT NULL,
    category character varying(30) NOT NULL,
    date timestamp without time zone NOT NULL,
    amount integer NOT NULL,
    note character varying(255),
    user_id integer NOT NULL
);


ALTER TABLE transactions OWNER TO marci;

--
-- Name: transactions_id_seq; Type: SEQUENCE; Schema: public; Owner: marci
--

CREATE SEQUENCE transactions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE transactions_id_seq OWNER TO marci;

--
-- Name: transactions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: marci
--

ALTER SEQUENCE transactions_id_seq OWNED BY transactions.id;


--
-- Name: transactions_user_id_seq; Type: SEQUENCE; Schema: public; Owner: marci
--

CREATE SEQUENCE transactions_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE transactions_user_id_seq OWNER TO marci;

--
-- Name: transactions_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: marci
--

ALTER SEQUENCE transactions_user_id_seq OWNED BY transactions.user_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: marci
--

CREATE TABLE users (
    id integer NOT NULL,
    name character varying(15) NOT NULL,
    e_mail character varying(255) NOT NULL
);


ALTER TABLE users OWNER TO marci;

--
-- Name: id; Type: DEFAULT; Schema: public; Owner: marci
--

ALTER TABLE ONLY categories ALTER COLUMN id SET DEFAULT nextval('categories_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: marci
--

ALTER TABLE ONLY transactions ALTER COLUMN id SET DEFAULT nextval('transactions_id_seq'::regclass);


--
-- Name: user_id; Type: DEFAULT; Schema: public; Owner: marci
--

ALTER TABLE ONLY transactions ALTER COLUMN user_id SET DEFAULT nextval('transactions_user_id_seq'::regclass);


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: marci
--

COPY categories (id, category, transaction_type) FROM stdin;
\.


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: marci
--

SELECT pg_catalog.setval('categories_id_seq', 1, false);


--
-- Data for Name: transactions; Type: TABLE DATA; Schema: public; Owner: marci
--

COPY transactions (id, category, date, amount, note, user_id) FROM stdin;
\.


--
-- Name: transactions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: marci
--

SELECT pg_catalog.setval('transactions_id_seq', 1, false);


--
-- Name: transactions_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: marci
--

SELECT pg_catalog.setval('transactions_user_id_seq', 1, false);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: marci
--

COPY users (id, name, e_mail) FROM stdin;
\.


--
-- Name: users_id_pk; Type: CONSTRAINT; Schema: public; Owner: marci
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_id_pk PRIMARY KEY (id);


--
-- Name: transactions_fk; Type: FK CONSTRAINT; Schema: public; Owner: marci
--

ALTER TABLE ONLY transactions
    ADD CONSTRAINT transactions_fk FOREIGN KEY (user_id) REFERENCES users(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

