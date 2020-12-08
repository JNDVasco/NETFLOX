create table historico_artigos
(
    id_art         serial not null
        constraint historico_artigos_pkey
            primary key,
    preco_anterior bigint,
    data_mudanca   date,
    artigos_id_art bigint
        constraint historico_artigos_fk1
            references artigos
);

alter table historico_artigos
    owner to lbkoexwzuhsloo;

