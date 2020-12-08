create table mensagem
(
    id_msg                 serial not null
        constraint mensagem_pkey
            primary key,
    corpo                  text,
    mensagens_n_lidas      boolean,
    admin_pessoa_id_pessoa bigint
        constraint mensagem_fk1
            references admin
);

alter table mensagem
    owner to lbkoexwzuhsloo;

