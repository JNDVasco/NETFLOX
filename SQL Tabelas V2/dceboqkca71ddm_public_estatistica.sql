create table estatistica
(
    id_estatistica        serial not null
        constraint estatistica_pkey
            primary key,
    total_clientes        bigint,
    total_artigos         bigint,
    valor_total_alugados  bigint,
    valor_total_alugueres boolean,
    total_art_por_tipo    bigint,
    tempo_total_alugado   bigint,
    tipo_mais_alugado     text
);

alter table estatistica
    owner to lbkoexwzuhsloo;

