-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 07, 2019 at 07:32 PM
-- Server version: 10.1.35-MariaDB
-- PHP Version: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sliit_att`
--

-- --------------------------------------------------------

--
-- Table structure for table `fo_dd`
--

CREATE TABLE `fo_dd` (
  `id` varchar(10) NOT NULL,
  `name` varchar(255) NOT NULL,
  `fing` varchar(255) NOT NULL,
  `week1` int(1) NOT NULL,
  `week2` int(1) NOT NULL,
  `week3` int(1) NOT NULL,
  `week4` int(1) NOT NULL,
  `week5` int(1) NOT NULL,
  `week6` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fo_dd`
--

INSERT INTO `fo_dd` (`id`, `name`, `fing`, `week1`, `week2`, `week3`, `week4`, `week5`, `week6`) VALUES
('en16507616', 'B.T.G.M Kariyawasam', '222', 0, 0, 0, 0, 0, 0),
('en16504263', 'N.D.S Arachchige', '222', 0, 0, 0, 0, 0, 0),
('en16504262', 'K.K.A.P Kodithuwakku', '222', 1, 0, 0, 0, 0, 0),
('en16504261', 'Damindu Welikala', '222', 1, 1, 0, 0, 0, 0),
('en16509214', 'daham de silva', '222', 0, 0, 0, 0, 0, 0),
('en16504264', 'S.A.K Pathirana', '222', 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `im_mm`
--

CREATE TABLE `im_mm` (
  `id` varchar(10) NOT NULL,
  `name` varchar(255) NOT NULL,
  `fing` varchar(255) NOT NULL,
  `week1` int(1) NOT NULL,
  `week2` int(1) NOT NULL,
  `week3` int(1) NOT NULL,
  `week4` int(1) NOT NULL,
  `week5` int(1) NOT NULL,
  `week6` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `im_mm`
--

INSERT INTO `im_mm` (`id`, `name`, `fing`, `week1`, `week2`, `week3`, `week4`, `week5`, `week6`) VALUES
('en16504260', 'Samitha Wijekoon', '222', 0, 0, 0, 0, 0, 0),
('en16504263', 'N.D.S Arachchige', '3a28ab5c879d24d67ce89f5f51a64f945b5967f0dab48510db4ab727130d6e61', 1, 0, 0, 0, 0, 0),
('en16504264', 'S.A.K Pathirana', '59ea4846251468183bd6097afff2aa1479868fc71ef19348c8ca1964cccb5349', 1, 0, 0, 0, 0, 0),
('en16504261', 'Damindu Welikala', '222', 0, 0, 0, 0, 0, 0),
('en16504262', 'K.K.A.P Kodithuwakku', '222', 0, 0, 0, 0, 0, 0),
('en16507616', 'B.T.G.M Kariyawasam', '222', 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `in_en`
--

CREATE TABLE `in_en` (
  `id` varchar(10) NOT NULL,
  `name` varchar(255) NOT NULL,
  `fing` varchar(255) NOT NULL,
  `week1` int(1) NOT NULL,
  `week2` int(1) NOT NULL,
  `week3` int(1) NOT NULL,
  `week4` int(1) NOT NULL,
  `week5` int(1) NOT NULL,
  `week6` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `in_en`
--

INSERT INTO `in_en` (`id`, `name`, `fing`, `week1`, `week2`, `week3`, `week4`, `week5`, `week6`) VALUES
('en16507616', 'B.T.G.M Kariyawasam', '222', 0, 0, 0, 0, 0, 0),
('en16504264', 'R.M.B.C.B Rathnayake', '222', 0, 0, 0, 0, 0, 0),
('en16504263', 'N.D.S Arachchige', '222', 1, 0, 0, 0, 0, 0),
('en16504262', 'K.K.A.P Kodithuwakku', '222', 1, 1, 0, 0, 0, 0),
('en16504261', 'Damindu Welikala', '222', 0, 0, 0, 0, 0, 0),
('en16509214', 'Daham De Silva', '222', 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `lecturers_info`
--

CREATE TABLE `lecturers_info` (
  `name` varchar(255) NOT NULL,
  `fing` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `lecturers_info`
--

INSERT INTO `lecturers_info` (`name`, `fing`) VALUES
('Saman Kumara', '3a28ab5c879d24d67ce89f5f51a64f945b5967f0dab48510db4ab727130d6e61'),
('Wasantha Senanayaka', 'fp3456'),
('Sugath Jayasinghe', 'fp8967'),
('Kumara Shantha', 'fp1411');

-- --------------------------------------------------------

--
-- Table structure for table `po_am`
--

CREATE TABLE `po_am` (
  `id` varchar(10) NOT NULL,
  `name` varchar(255) NOT NULL,
  `fing` varchar(255) NOT NULL,
  `week1` int(1) NOT NULL,
  `week2` int(1) NOT NULL,
  `week3` int(1) NOT NULL,
  `week4` int(1) NOT NULL,
  `week5` int(1) NOT NULL,
  `week6` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `po_am`
--

INSERT INTO `po_am` (`id`, `name`, `fing`, `week1`, `week2`, `week3`, `week4`, `week5`, `week6`) VALUES
('en16509214', 'Daham de Silva', '222', 0, 0, 0, 0, 0, 0),
('en16504263', 'N.D.S Arachchige', '222', 0, 0, 0, 0, 0, 0),
('en16504262', 'K.K.A.P Kodithuwakku', '222', 0, 0, 0, 0, 0, 0),
('en16504261', 'Damindu Welikala', '222', 0, 0, 0, 0, 0, 0),
('en16504260', 'Samitha Wijekoon', '222', 0, 0, 0, 0, 0, 0),
('en16504264', 'S.A.K Pathirana', '222', 0, 0, 0, 0, 0, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
