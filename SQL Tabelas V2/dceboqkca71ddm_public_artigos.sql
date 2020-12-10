create table artigos
(
    id_art         serial not null
        constraint artigos_pkey
            primary key,
    tipo           text,
    titulo         text,
    preco          bigint,
    tempo_para_ver bigint,
    detalhes       text
);

alter table artigos
    owner to lbkoexwzuhsloo;

INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (2, 'Série', 'The Queen''s Gambit ', 1056, 5, 'Orphaned at the tender age of nine, prodigious introvert Beth Harmon discovers and masters the game of chess in 1960s USA. But child stardom comes at a price.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (17, 'Filme', 'Hillbilly Elegy', 399, 1, 'An urgent phone call pulls a Yale Law student back to his Ohio hometown, where he reflects on three generations of family history and his own future.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (19, 'Filme', 'Tenet', 599, 2, 'Armed with only one word, Tenet, and fighting for the survival of the entire world, a Protagonist journeys through a twilight world of international espionage on a mission that will unfold in something beyond real time.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (13, 'Filme', 'Juno', 399, 3, 'Faced with an unplanned pregnancy, an offbeat young person makes an unusual decision regarding the unborn child.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (15, 'Filme', 'Life in a Year', 599, 1, 'The movie follows 17-year-old Daryn who finds out that his girlfriend is dying. He sets out to give her an entire life in the last year she has left.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (3, 'Série', 'Vikings ', 1199, 6, 'Vikings transports us to the brutal and mysterious world of Ragnar Lothbrok, a Viking warrior and farmer who yearns to explore - and raid - the distant shores across the ocean.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (16, 'Filme', 'Crónicas de Natal: Parte Dois', 399, 2, 'Kate Pierce, now a cynical teen, is unexpectedly reunited with Santa Claus when a mysterious troublemaker threatens to cancel Christmas - forever. ');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (12, 'Filme', 'Sozinho em Casa', 599, 2, 'An eight-year-old troublemaker must protect his house from a pair of burglars when he is accidentally left home alone by his family during Christmas vacation.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (8, 'Série', 'Star Trek: Discovery', 599, 4, 'Ten years before Kirk, Spock, and the Enterprise, the USS Discovery discovers new worlds and lifeforms as one Starfleet officer learns to understand all things alien.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (1, 'Série', 'The Mandalorian  ', 899, 4, 'The travels of a lone bounty hunter in the outer reaches of the galaxy, far from the authority of the New Republic.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (20, 'Filme', 'Amor com Data Marcada', 849, 1, 'Fed up with being single on holidays, two strangers agree to be each other''s platonic plus-ones all year long, only to catch real feelings along the way.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (9, 'Série', 'Star Wars: The Clone Wars  ', 899, 8, 'Jedi Knights lead the Grand Army of the Republic against the droid army of the Separatists.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (18, 'Filme', 'Happiest Season', 299, 1, 'A holiday romantic comedy that captures the range of emotions tied to wanting your family''s acceptance, being true to yourself, and trying not to ruin Christmas.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (14, 'Filme', 'Crónicas de Natal', 299, 1, 'The story of sister and brother, Kate and Teddy Pierce, whose Christmas Eve plan to catch Santa Claus on camera turns into an unexpected journey that most kids could only dream about.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (7, 'Série', 'The Walking Dead', 1199, 4, 'Sheriff Deputy Rick Grimes wakes up from a coma to learn the world is in ruins and must lead a group of survivors to stay alive. ');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (10, 'Série', 'Peaky Blinders ', 1200, 6, 'A gangster family epic set in 1900s England, centering on a gang who sew razor blades in the peaks of their caps, and their fierce boss Tommy Shelby.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (4, 'Série', 'Anatomia de Grey', 899, 7, 'A drama centered on the personal and professional lives of five surgical interns and their supervisors.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (5, 'Série', 'A Guerra dos Tronos', 899, 6, 'Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (11, 'Filme', 'Mulan', 299, 1, 'A young Chinese maiden disguises herself as a male warrior in order to save her father.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (6, 'Série', 'The Boys  ', 1260, 6, 'A group of vigilantes set out to take down corrupt superheroes who abuse their superpowers.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (21, 'Documentário', 'Alien Worlds', 799, 1, 'Applying the laws of life on Earth to rest of the galaxy, this series blends science facts and fiction to imagine alien life on other planets.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (22, 'Documentário', 'Murder on Middle Beach', 399, 2, 'A young man is determined to solve an unspeakable crime and absolve the people he loves, while looking for answers within his fractured family and community.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (23, 'Documentário', 'Mosul', 1010, 1, 'The gritty, thrilling story of local militias and uneasy allies who banded together to liberate Iraq''s second-largest city of 1.3 million people from ISIS in 2017.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (24, 'Documentário', 'Diego Maradona', 550, 2, 'Constructed from over 500 hours of never-before-seen footage, this documentary centers on the career of celebrated football player Diego Maradona, who played for S.S.C. Napoli in the 1980s.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (25, 'Documentário', 'How to with John Wilson', 199, 1, 'An anxious New Yorker who attempts to give everyday advice while dealing with his own personal issues.');
INSERT INTO public.artigos (id_art, tipo, titulo, preco, tempo_para_ver, detalhes) VALUES (26, 'Documentário', 'The Social Dilemma ', 1230, 3, 'Explores the dangerous human impact of social networking, with tech experts sounding the alarm on their own creations.');