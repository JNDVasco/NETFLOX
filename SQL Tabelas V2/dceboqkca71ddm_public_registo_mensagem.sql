create table registo_mensagem
(
    id_registo      serial not null
        constraint registo_mensagem_pkey
            primary key,
    mensagens_lidas bigint,
    mensagem_id_msg bigint
        constraint registo_mensagem_fk1
            references mensagem
);

alter table registo_mensagem
    owner to lbkoexwzuhsloo;

