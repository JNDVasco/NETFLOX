create table admin
(
    codigo_seg       bigint,
    pessoa_id_pessoa serial not null
        constraint admin_pkey
            primary key,
    pessoa_email     text,
    pessoa_nome      text,
    pessoa_password  text
);

alter table admin
    owner to lbkoexwzuhsloo;

