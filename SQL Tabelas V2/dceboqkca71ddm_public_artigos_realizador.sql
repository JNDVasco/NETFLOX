create table artigos_realizador
(
    artigos_id_art           bigint not null
        constraint artigos_realizador_fk1
            references artigos,
    realizador_id_realizador bigint not null
        constraint artigos_realizador_fk2
            references realizador,
    constraint artigos_realizador_pkey
        primary key (artigos_id_art, realizador_id_realizador)
);

alter table artigos_realizador
    owner to lbkoexwzuhsloo;

INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (11, 11);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (12, 12);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (13, 13);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (14, 14);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (15, 15);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (16, 12);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (17, 16);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (18, 17);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (19, 18);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (20, 19);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (1, 1);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (2, 2);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (3, 3);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (4, 4);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (5, 5);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (6, 6);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (7, 7);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (8, 8);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (9, 9);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (10, 10);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (21, 20);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (22, 21);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (23, 22);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (24, 23);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (25, 24);
INSERT INTO public.artigos_realizador (artigos_id_art, realizador_id_realizador) VALUES (26, 25);