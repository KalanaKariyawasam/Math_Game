-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 09, 2020 at 04:08 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `math_game`
--

-- --------------------------------------------------------

--
-- Table structure for table `past_player_details`
--

CREATE TABLE `past_player_details` (
  `name` varchar(50) NOT NULL,
  `gamemode` varchar(50) NOT NULL,
  `correctquestions` int(11) NOT NULL,
  `totalquestions` int(11) NOT NULL,
  `precentage` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `past_player_details`
--

INSERT INTO `past_player_details` (`name`, `gamemode`, `correctquestions`, `totalquestions`, `precentage`) VALUES
('Kalana', 'Quick', 5, 5, 100),
('Himesh', 'Easy', 10, 10, 100),
('Shazan', 'Medium', 5, 5, 100),
('Chamantha', 'Hard', 6, 10, 60),
('Tharusha', 'Difficult', 4, 5, 80),
('Piyumika', 'Easy', 10, 10, 100);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
