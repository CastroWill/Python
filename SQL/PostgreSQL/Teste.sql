CREATE TABLE estoque
(
	codigo integer,
	produto character varying(100),
	categoria character varying(100),
	marca character varying(100),
	preco numeric (10, 2),
	quantidade integer
);

SELECT * FROM public.estoque

DELETE FROM estoque

DROP TABLE estoque

copy estoque(codigo, produto, categoria, marca, preco, quantidade)  from 'D:/estoque_21032021.csv' with delimiter as ';' CSV HEADER