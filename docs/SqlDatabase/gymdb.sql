-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-08-2023 a las 22:17:52
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gymdb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diet`
--

CREATE TABLE `diet` (
  `id` int(11) NOT NULL,
  `description` text NOT NULL,
  `status` tinyint(4) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `exercise_kit`
--

CREATE TABLE `exercise_kit` (
  `id` int(11) NOT NULL,
  `routine` text NOT NULL,
  `routine_days` int(11) NOT NULL,
  `exercise_start` date NOT NULL,
  `routine_plan_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`id`, `name`) VALUES
(1, 'usuario'),
(2, 'entrenador'),
(3, 'Admin');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `routine_plan`
--

CREATE TABLE `routine_plan` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `days_plan` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tpay`
--

CREATE TABLE `tpay` (
  `id` int(11) NOT NULL,
  `amount` int(11) DEFAULT NULL,
  `payment_credit` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `number` varchar(45) NOT NULL,
  `address` text NOT NULL,
  `name` varchar(75) NOT NULL,
  `status` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `number`, `address`, `name`, `status`) VALUES
(1, '0-555', 'barrancas', 'Paco A.', 'activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_acces`
--

CREATE TABLE `user_acces` (
  `id` int(11) NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `user_id` int(11) NOT NULL,
  `rol_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `user_acces`
--

INSERT INTO `user_acces` (`id`, `user_name`, `password`, `user_id`, `rol_id`) VALUES
(1, 'root', '123', 1, 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `diet`
--
ALTER TABLE `diet`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_diet_user_idx` (`user_id`);

--
-- Indices de la tabla `exercise_kit`
--
ALTER TABLE `exercise_kit`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_exercise_kit_routine_plan1_idx` (`routine_plan_id`),
  ADD KEY `fk_exercise_kit_user1_idx` (`user_id`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `routine_plan`
--
ALTER TABLE `routine_plan`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tpay`
--
ALTER TABLE `tpay`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_tPay_user1_idx` (`user_id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `user_acces`
--
ALTER TABLE `user_acces`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_user_acces_user1_idx` (`user_id`),
  ADD KEY `fk_user_acces_rol1_idx` (`rol_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `diet`
--
ALTER TABLE `diet`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `exercise_kit`
--
ALTER TABLE `exercise_kit`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `routine_plan`
--
ALTER TABLE `routine_plan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tpay`
--
ALTER TABLE `tpay`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `user_acces`
--
ALTER TABLE `user_acces`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `diet`
--
ALTER TABLE `diet`
  ADD CONSTRAINT `fk_diet_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `exercise_kit`
--
ALTER TABLE `exercise_kit`
  ADD CONSTRAINT `fk_exercise_kit_routine_plan1` FOREIGN KEY (`routine_plan_id`) REFERENCES `routine_plan` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_exercise_kit_user1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `tpay`
--
ALTER TABLE `tpay`
  ADD CONSTRAINT `fk_tPay_user1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `user_acces`
--
ALTER TABLE `user_acces`
  ADD CONSTRAINT `fk_user_acces_rol1` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_user_acces_user1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
