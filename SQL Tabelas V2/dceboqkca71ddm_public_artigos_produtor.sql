create table artigos_produtor
(
    artigos_id_art       bigint not null
        constraint artigos_produtor_fk1
            references artigos,
    produtor_id_produtor bigint not null
        constraint artigos_produtor_fk2
            references produtor,
    constraint artigos_produtor_pkey
        primary key (artigos_id_art, produtor_id_produtor)
);

alter table artigos_produtor
    owner to lbkoexwzuhsloo;

INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (11, 1);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (12, 2);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (13, 3);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (14, 4);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (15, 5);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (16, 4);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (17, 6);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (18, 7);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (19, 8);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (20, 9);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (21, 10);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (22, 11);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (23, 12);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (24, 13);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (25, 14);
INSERT INTO public.artigos_produtor (artigos_id_art, produtor_id_produtor) VALUES (26, 15);