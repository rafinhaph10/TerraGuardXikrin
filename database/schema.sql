CREATE EXTENSION IF NOT EXISTS postgis;

----------------------------------------------------
-- ÁREAS MONITORADAS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS areas (

    id SERIAL PRIMARY KEY,

    nome VARCHAR(200) NOT NULL,

    descricao TEXT,

    tipo VARCHAR(100),

    origem VARCHAR(100),

    responsavel VARCHAR(150),

    ativo BOOLEAN DEFAULT TRUE,

    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    srid INTEGER DEFAULT 4326,

    area_ha DOUBLE PRECISION,

    perimetro_m DOUBLE PRECISION,

    bbox TEXT,

    geometry geometry(MULTIPOLYGON,4326),

    centroide geometry(POINT,4326)

);

----------------------------------------------------
-- FOCOS DE CALOR
----------------------------------------------------

CREATE TABLE IF NOT EXISTS focos (

    id SERIAL PRIMARY KEY,

    fonte VARCHAR(50),

    satelite VARCHAR(100),

    data_hora TIMESTAMP,

    frp DOUBLE PRECISION,

    confianca DOUBLE PRECISION,

    risco_fogo DOUBLE PRECISION,

    precipitacao DOUBLE PRECISION,

    latitude DOUBLE PRECISION,

    longitude DOUBLE PRECISION,

    municipio VARCHAR(150),

    estado VARCHAR(100),

    pais VARCHAR(100),

    bioma VARCHAR(100),

    geometry geometry(POINT,4326)

);

----------------------------------------------------
-- ALERTAS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS alertas (

    id SERIAL PRIMARY KEY,

    foco_id INTEGER REFERENCES focos(id),

    area_id INTEGER REFERENCES areas(id),

    tipo VARCHAR(100),

    status VARCHAR(50),

    observacao TEXT,

    data_alerta TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

----------------------------------------------------
-- MONITORAMENTOS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS monitoramentos (

    id SERIAL PRIMARY KEY,

    origem VARCHAR(100),

    data_execucao TIMESTAMP,

    focos_encontrados INTEGER,

    tempo_execucao DOUBLE PRECISION,

    observacao TEXT

);

----------------------------------------------------
-- USUÁRIOS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS usuarios (

    id SERIAL PRIMARY KEY,

    nome VARCHAR(150),

    email VARCHAR(150) UNIQUE,

    senha_hash TEXT,

    perfil VARCHAR(50),

    ativo BOOLEAN DEFAULT TRUE,

    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);