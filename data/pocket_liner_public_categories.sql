DROP TABLE IF EXISTS public.categories
CREATE TABLE public.categories
(
    id integer DEFAULT nextval('categories_id_seq'::regclass) NOT NULL,
    category varchar(255) NOT NULL,
    income boolean NOT NULL
);
INSERT INTO public.categories (id, category, income) VALUES (5, 'Gift', true);
INSERT INTO public.categories (id, category, income) VALUES (6, 'Salary', true);
INSERT INTO public.categories (id, category, income) VALUES (7, 'Income - Else', true);
INSERT INTO public.categories (id, category, income) VALUES (8, 'Pension', true);
INSERT INTO public.categories (id, category, income) VALUES (9, 'Food', false);
INSERT INTO public.categories (id, category, income) VALUES (10, 'Health', false);
INSERT INTO public.categories (id, category, income) VALUES (11, 'Clothes', false);
INSERT INTO public.categories (id, category, income) VALUES (12, 'Entertainment', false);
INSERT INTO public.categories (id, category, income) VALUES (13, 'Bills', false);
INSERT INTO public.categories (id, category, income) VALUES (14, 'Vacation', false);
INSERT INTO public.categories (id, category, income) VALUES (15, 'Kids', false);
INSERT INTO public.categories (id, category, income) VALUES (16, 'Travel', false);
INSERT INTO public.categories (id, category, income) VALUES (17, 'Sports', false);
INSERT INTO public.categories (id, category, income) VALUES (18, 'Car', false);
INSERT INTO public.categories (id, category, income) VALUES (19, 'Housekeeping', false);
INSERT INTO public.categories (id, category, income) VALUES (20, 'Expense - Else', false);
