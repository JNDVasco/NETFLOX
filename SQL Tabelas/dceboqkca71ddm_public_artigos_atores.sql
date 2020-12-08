create table artigos_atores
(
    artigos_id_art bigint not null
        constraint artigos_atores_fk1
            references artigos,
    atores_id_ator bigint not null
        constraint artigos_atores_fk2
            references atores,
    constraint artigos_atores_pkey
        primary key (artigos_id_art, atores_id_ator)
);

alter table artigos_atores
    owner to lbkoexwzuhsloo;

INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (1, 25);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (1, 26);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (1, 27);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (2, 22);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (2, 23);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (2, 24);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (3, 19);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (3, 20);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (3, 21);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (4, 18);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (4, 17);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (4, 16);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (5, 15);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (5, 14);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (5, 13);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (6, 1);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (6, 2);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (10, 29);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (6, 3);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (10, 30);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (7, 4);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (7, 5);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (7, 6);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (8, 10);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (8, 11);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (8, 12);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (9, 7);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (9, 8);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (9, 9);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (10, 28);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (11, 31);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (11, 32);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (11, 33);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (12, 34);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (12, 35);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (12, 36);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (13, 37);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (13, 38);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (13, 39);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (14, 40);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (14, 41);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (14, 42);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (15, 43);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (15, 44);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (15, 45);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (16, 40);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (16, 46);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (16, 41);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (17, 47);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (17, 48);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (17, 49);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (18, 50);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (18, 51);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (18, 52);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (19, 53);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (19, 54);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (19, 55);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (20, 56);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (20, 57);
INSERT INTO public.artigos_atores (artigos_id_art, atores_id_ator) VALUES (20, 58);