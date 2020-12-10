create table produtor
(
    id_produtor   serial not null
        constraint produtor_pkey
            primary key,
    primeiro_nome text,
    segundo_nome  text
);

alter table produtor
    owner to lbkoexwzuhsloo;

INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (1, 'Chris', 'Bender');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (2, 'Tarquin', 'Gotch');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (3, 'Joseph', 'Drake');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (4, 'Bill', 'Andrew');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (5, 'Marc', 'Bienstock ');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (6, 'William', 'M. Connor');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (7, 'Marty', 'Bowen');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (9, 'Mary', 'Viola');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (8, 'Emma', 'Thomas');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (11, 'Sara', 'Rodriguez');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (15, 'Larissa', 'Rhodes');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (14, 'Nathan', 'Fielder');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (13, 'Paul', 'Martin');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (12, 'Matt', 'Schrader');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (10, 'Lynn', 'Philpott');