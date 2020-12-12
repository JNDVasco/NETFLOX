CREATE TABLE cliente (
	saldo		 BIGINT DEFAULT 2000,
	pessoa_id_pessoa BIGINT,
	pessoa_email	 TEXT(512),
	pessoa_nome	 TEXT(512),
	pessoa_password	 TEXT(512),
	PRIMARY KEY(pessoa_id_pessoa)
);

CREATE TABLE artigos (
	id_art	 BIGINT,
	tipo		 TEXT(512),
	titulo	 TEXT(512),
	preco		 BIGINT,
	tempo_para_ver BIGINT,
	detalhes	 TEXT(512),
	PRIMARY KEY(id_art)
);

CREATE TABLE admin (
	codigo_seg	 BIGINT,
	pessoa_id_pessoa BIGINT,
	pessoa_email	 TEXT(512),
	pessoa_nome	 TEXT(512),
	pessoa_password	 TEXT(512),
	PRIMARY KEY(pessoa_id_pessoa)
);

CREATE TABLE mensagem (
	id_msg		 BIGINT,
	corpo			 TEXT(512),
	mensagens_lida	 BOOL,
	assunto		 TEXT(512),
	admin_pessoa_id_pessoa BIGINT,
	PRIMARY KEY(id_msg)
);

CREATE TABLE estatistica (
	id_estatistica	 BIGINT,
	total_clientes	 BIGINT,
	total_artigos	 BIGINT,
	valor_total_alugados	 BIGINT,
	valor_total_alugueres BIGINT,
	total_art_por_tipo	 BIGINT,
	tempo_total_alugado	 BIGINT,
	saldo_total_clientes	 BIGINT,
	PRIMARY KEY(id_estatistica)
);

CREATE TABLE historico_artigos (
	id_art	 BIGINT,
	preco_anterior BIGINT,
	data_mudanca	 BIGINT,
	artigos_id_art BIGINT,
	PRIMARY KEY(id_art)
);

CREATE TABLE atores (
	id_ator	 BIGINT,
	primeiro_nome TEXT(512),
	segundo_nome	 TEXT(512),
	PRIMARY KEY(id_ator)
);

CREATE TABLE realizador (
	id_realizador BIGINT,
	primeiro_nome TEXT(512),
	segundo_nome	 TEXT(512),
	PRIMARY KEY(id_realizador)
);

CREATE TABLE produtor (
	id_produtor	 BIGINT,
	primeiro_nome TEXT(512),
	segundo_nome	 TEXT(512),
	PRIMARY KEY(id_produtor)
);

CREATE TABLE aluguer (
	id_aluguer		 BIGINT,
	data			 BIGINT,
	preco			 BIGINT,
	data_validade		 DATE,
	tempo_para_ver		 BIGINT,
	artigos_id_art		 BIGINT NOT NULL,
	cliente_pessoa_id_pessoa BIGINT NOT NULL,
	PRIMARY KEY(id_aluguer)
);

CREATE TABLE registo_mensagem (
	id_registo	 BIGINT,
	mensagens_lidas BIGINT,
	mensagem_id_msg BIGINT,
	PRIMARY KEY(id_registo)
);

CREATE TABLE artigos_produtor (
	artigos_id_art	 BIGINT,
	produtor_id_produtor BIGINT,
	PRIMARY KEY(artigos_id_art,produtor_id_produtor)
);

CREATE TABLE artigos_realizador (
	artigos_id_art		 BIGINT,
	realizador_id_realizador BIGINT,
	PRIMARY KEY(artigos_id_art,realizador_id_realizador)
);

CREATE TABLE artigos_atores (
	artigos_id_art BIGINT,
	atores_id_ator BIGINT,
	PRIMARY KEY(artigos_id_art,atores_id_ator)
);

CREATE TABLE cliente_mensagem (
	cliente_pessoa_id_pessoa BIGINT,
	mensagem_id_msg		 BIGINT,
	PRIMARY KEY(cliente_pessoa_id_pessoa,mensagem_id_msg)
);

CREATE TABLE cliente_artigos (
	cliente_pessoa_id_pessoa BIGINT,
	artigos_id_art		 BIGINT,
	PRIMARY KEY(cliente_pessoa_id_pessoa,artigos_id_art)
);

CREATE TABLE admin_artigos (
	admin_pessoa_id_pessoa BIGINT,
	artigos_id_art	 BIGINT,
	PRIMARY KEY(admin_pessoa_id_pessoa,artigos_id_art)
);

ALTER TABLE mensagem ADD CONSTRAINT mensagem_fk1 FOREIGN KEY (admin_pessoa_id_pessoa) REFERENCES admin(pessoa_id_pessoa);
ALTER TABLE historico_artigos ADD CONSTRAINT historico_artigos_fk1 FOREIGN KEY (artigos_id_art) REFERENCES artigos(id_art);
ALTER TABLE aluguer ADD CONSTRAINT aluguer_fk1 FOREIGN KEY (artigos_id_art) REFERENCES artigos(id_art);
ALTER TABLE aluguer ADD CONSTRAINT aluguer_fk2 FOREIGN KEY (cliente_pessoa_id_pessoa) REFERENCES cliente(pessoa_id_pessoa);
ALTER TABLE registo_mensagem ADD CONSTRAINT registo_mensagem_fk1 FOREIGN KEY (mensagem_id_msg) REFERENCES mensagem(id_msg);
ALTER TABLE artigos_produtor ADD CONSTRAINT artigos_produtor_fk1 FOREIGN KEY (artigos_id_art) REFERENCES artigos(id_art);
ALTER TABLE artigos_produtor ADD CONSTRAINT artigos_produtor_fk2 FOREIGN KEY (produtor_id_produtor) REFERENCES produtor(id_produtor);
ALTER TABLE artigos_realizador ADD CONSTRAINT artigos_realizador_fk1 FOREIGN KEY (artigos_id_art) REFERENCES artigos(id_art);
ALTER TABLE artigos_realizador ADD CONSTRAINT artigos_realizador_fk2 FOREIGN KEY (realizador_id_realizador) REFERENCES realizador(id_realizador);
ALTER TABLE artigos_atores ADD CONSTRAINT artigos_atores_fk1 FOREIGN KEY (artigos_id_art) REFERENCES artigos(id_art);
ALTER TABLE artigos_atores ADD CONSTRAINT artigos_atores_fk2 FOREIGN KEY (atores_id_ator) REFERENCES atores(id_ator);
ALTER TABLE cliente_mensagem ADD CONSTRAINT cliente_mensagem_fk1 FOREIGN KEY (cliente_pessoa_id_pessoa) REFERENCES cliente(pessoa_id_pessoa);
ALTER TABLE cliente_mensagem ADD CONSTRAINT cliente_mensagem_fk2 FOREIGN KEY (mensagem_id_msg) REFERENCES mensagem(id_msg);
ALTER TABLE cliente_artigos ADD CONSTRAINT cliente_artigos_fk1 FOREIGN KEY (cliente_pessoa_id_pessoa) REFERENCES cliente(pessoa_id_pessoa);
ALTER TABLE cliente_artigos ADD CONSTRAINT cliente_artigos_fk2 FOREIGN KEY (artigos_id_art) REFERENCES artigos(id_art);
ALTER TABLE admin_artigos ADD CONSTRAINT admin_artigos_fk1 FOREIGN KEY (admin_pessoa_id_pessoa) REFERENCES admin(pessoa_id_pessoa);
ALTER TABLE admin_artigos ADD CONSTRAINT admin_artigos_fk2 FOREIGN KEY (artigos_id_art) REFERENCES artigos(id_art);

