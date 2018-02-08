DROP TABLE IF EXISTS public.transactions
CREATE TABLE public.transactions
(
    id integer DEFAULT nextval('transactions_id_seq'::regclass) NOT NULL,
    category varchar(30) NOT NULL,
    date timestamp NOT NULL,
    amount integer NOT NULL,
    note varchar(255),
    user_id integer DEFAULT nextval('transactions_user_id_seq'::regclass) NOT NULL,
    CONSTRAINT transactions_fk FOREIGN KEY (user_id) REFERENCES users (id)
);
INSERT INTO public.transactions (id, category, date, amount, note, user_id) VALUES (13, 'Food', '2018-01-29 00:00:00.000000', 1800, 'Pizza Margherita', 1);
INSERT INTO public.transactions (id, category, date, amount, note, user_id) VALUES (14, 'Bills', '2018-02-04 00:00:00.000000', 38000, 'Car insurance', 1);
INSERT INTO public.transactions (id, category, date, amount, note, user_id) VALUES (15, 'Salary', '2018-02-05 00:00:00.000000', 280000, 'Feb. Salary', 1);
