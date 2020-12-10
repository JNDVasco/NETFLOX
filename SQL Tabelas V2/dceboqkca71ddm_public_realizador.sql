create table realizador
(
    id_realizador serial not null
        constraint realizador_pkey
            primary key,
    primeiro_nome text,
    segundo_nome  text
);

alter table realizador
    owner to lbkoexwzuhsloo;

INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (11, 'Niki', 'Caro');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (12, 'Chris', 'Columbus');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (13, 'Jason', 'Reitman');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (15, 'Mitja', 'Okorn');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (14, 'Clay', 'Kaytis');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (19, 'Jonh', 'Whitesell');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (17, 'Clea', 'DuVall');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (18, 'Christopher', 'Nolan');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (16, 'Ron', 'Howard');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (2, 'Scott', 'Frank');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (5, 'David', 'Nutter');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (8, 'Olatunde', 'Osunsanmi');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (9, 'Dave', 'Filoni');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (7, 'Greg', 'Nicotero');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (3, 'Ciaran', 'Donnelly');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (10, 'Colm', 'McCarthy');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (4, 'Rob', 'Corn');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (6, 'Philip', 'Sgriccia');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (1, 'Rick', 'Famuyiwa ');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (20, 'Suzy', 'Boyles');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (21, 'Madison', 'Hamburg');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (22, 'Daniel', 'Grabriel');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (23, 'Asif', 'Kapadia');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (24, 'John', 'Wilson');
INSERT INTO public.realizador (id_realizador, primeiro_nome, segundo_nome) VALUES (25, 'Jeff', 'Orlowski');