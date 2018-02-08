DROP TABLE IF EXISTS public.users
CREATE TABLE public.users
(
    id integer DEFAULT nextval('users_id_seq'::regclass) PRIMARY KEY NOT NULL,
    name varchar(15) NOT NULL,
    e_mail varchar(255) NOT NULL,
    pass_hash varchar(255) NOT NULL
);
CREATE UNIQUE INDEX users_e_mail_uindex ON public.users (e_mail);
INSERT INTO public.users (id, name, e_mail, pass_hash) VALUES (1, 'Marci', 'Lol@gmail.com', '$2b$12$MhWQasZIg.WApVpK7rW0DOPTaQ0z.1OmEKQm3wCXMd9phXNztpE2m');
INSERT INTO public.users (id, name, e_mail, pass_hash) VALUES (27, 'sadassdsad', 'dasdasdasd', '$2b$12$xbYOQ.O4TAP/71aNOGNWM.iGUCw.Sjh7JSWlFD3Z.6c0sETzPYAXW');
INSERT INTO public.users (id, name, e_mail, pass_hash) VALUES (28, 'wut', 'diz', '$2b$12$3v4vLLFWG4iTvUCTcqU3puiG../mq9z4SxyaZm.JFE5XZCJjh473.');
