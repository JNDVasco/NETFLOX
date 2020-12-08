create table cliente
(
    saldo            bigint default 20,
    pessoa_id_pessoa serial not null
        constraint cliente_pkey
            primary key,
    pessoa_email     text,
    pessoa_nome      text,
    pessoa_password  text
);

alter table cliente
    owner to lbkoexwzuhsloo;

