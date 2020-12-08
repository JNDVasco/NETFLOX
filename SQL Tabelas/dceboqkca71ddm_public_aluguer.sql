create table aluguer
(
    id_aluguer               serial not null
        constraint aluguer_pkey
            primary key,
    data                     date,
    preco                    bigint,
    data_validade            date,
    artigos_id_art           bigint not null
        constraint aluguer_fk1
            references artigos,
    cliente_pessoa_id_pessoa bigint not null
        constraint aluguer_fk2
            references cliente
);

alter table aluguer
    owner to lbkoexwzuhsloo;

