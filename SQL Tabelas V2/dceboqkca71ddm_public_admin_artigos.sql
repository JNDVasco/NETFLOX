create table admin_artigos
(
    admin_pessoa_id_pessoa bigint not null
        constraint admin_artigos_fk1
            references admin,
    artigos_id_art         bigint not null
        constraint admin_artigos_fk2
            references artigos,
    constraint admin_artigos_pkey
        primary key (admin_pessoa_id_pessoa, artigos_id_art)
);

alter table admin_artigos
    owner to lbkoexwzuhsloo;

