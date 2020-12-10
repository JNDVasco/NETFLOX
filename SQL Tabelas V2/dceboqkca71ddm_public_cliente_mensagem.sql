create table cliente_mensagem
(
    cliente_pessoa_id_pessoa bigint not null
        constraint cliente_mensagem_fk1
            references cliente,
    mensagem_id_msg          bigint not null
        constraint cliente_mensagem_fk2
            references mensagem,
    constraint cliente_mensagem_pkey
        primary key (cliente_pessoa_id_pessoa, mensagem_id_msg)
);

alter table cliente_mensagem
    owner to lbkoexwzuhsloo;

