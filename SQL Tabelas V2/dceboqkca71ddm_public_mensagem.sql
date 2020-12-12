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

INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa) VALUES (1, 'Mensagem de Teste', true, 2);
INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa) VALUES (2, 'Mensagem de Teste', true, 2);
INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa) VALUES (3, 'Mensagem de Teste', true, 2);
INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa) VALUES (4, 'Mensagem de Teste', false, 2);
INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa) VALUES (5, 'Mensagem de Teste', true, 2);