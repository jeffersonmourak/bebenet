SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE SCHEMA IF NOT EXISTS `BDnet`
  DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE `BDnet`; 

CREATE TABLE IF NOT EXISTS `usuario`(
  `cpf`varchar(15) NOT NULL, 
  `nome` varchar(100) NOT NULL,
  `idade` int(2) NOT NULL, 
  `nFilhos` int(2) NOT NULL,
  `login` varchar(20) NOT NULL,
  `senha` varchar(20) NOT NULL,
  PRIMARY KEY(`cpf`),
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC)
)ENGINE=InnoDB DEFAULT CHARSET = utf8;

CREATE TABLE IF NOT EXISTS `produto`(
  `codigo` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `pontuacao` int(3) ,
  `descricao` varchar(200),
  PRIMARY KEY(`codigo`),
  UNIQUE INDEX `codigo_UNIQUE` (`codigo` ASC)
)ENGINE=InnoDB DEFAULT CHARSET = utf8;

CREATE TABLE IF NOT EXISTS `interesse`(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `descricao` varchar(200) ,
    PRIMARY KEY (`id`),
      UNIQUE INDEX `id_UNIQUE` (`id` ASC)
)ENGINE=InnoDB DEFAULT CHARSET = utf8;

CREATE TABLE IF NOT EXISTS `operacao`(
  `tipo` int(1) NOT NULL,
  `data` DATE  NOT NULL,
  `hora` TIME  NOT NULL,
    `op_prod` int(11) NOT NULL,
  `u1` varchar(15) NOT NULL,
    `u2` varchar(15) NOT NULL,
  `valor` float(10,2),
  PRIMARY KEY(`op_prod`,`data`,`hora`),

CONSTRAINT `fk_u1`
      FOREIGN KEY (`u1`)
        REFERENCES `BDnet`.`usuario`(`cpf`)
      ON DELETE CASCADE 
      ON UPDATE NO ACTION,
    
CONSTRAINT `fk_u2`
      FOREIGN KEY (`u2`)
      REFERENCES `BDnet`.`usuario`(`cpf`)
      ON DELETE CASCADE 
      ON UPDATE NO ACTION,

CONSTRAINT `fk_produto`
        FOREIGN KEY (`op_prod`)
        REFERENCES `BDnet`.`produto`(`codigo`)
        ON DELETE CASCADE 
        ON UPDATE NO ACTION
)ENGINE=InnoDB DEFAULT CHARSET = utf8;