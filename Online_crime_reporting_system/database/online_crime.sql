-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 07, 2021 at 06:08 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `online_crime`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE `complaint` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `reason` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `status` varchar(20) NOT NULL,
  `report` varchar(20) NOT NULL,
  `cdate` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`id`, `username`, `name`, `reason`, `address`, `status`, `report`, `cdate`) VALUES
(1, 'arun', 'cherry', 'fighting', 'trichy', 'Action Completed..', '1', 'Jan-06-2021'),
(3, 'admin', 'cherry', 'hhh', 'trichy', 'Complaint', '', '05-01-2020'),
(4, 'arun', 'cherry', 'eee', 'trichy', 'Complaint', '0', 'Jan-07-2021');

-- --------------------------------------------------------

--
-- Table structure for table `crimes`
--

CREATE TABLE `crimes` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `image` varchar(50) NOT NULL,
  `ctype` varchar(50) NOT NULL,
  `address` varchar(200) NOT NULL,
  `status` varchar(20) NOT NULL,
  `report` varchar(20) NOT NULL,
  `rdate` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `crimes`
--

INSERT INTO `crimes` (`id`, `username`, `image`, `ctype`, `address`, `status`, `report`, `rdate`) VALUES
(1, 'arun', 'bg8.jpg', 'kidnapping', 'thillainagar', 'Action Completed..', '1', 'Jan-06-2021'),
(2, 'arun', 'bg7.jpg', 'dddd', 'dddd', 'Complaint', '0', 'Jan-07-2021');

-- --------------------------------------------------------

--
-- Table structure for table `missing_person`
--

CREATE TABLE `missing_person` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `age` varchar(20) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `missing_place` varchar(100) NOT NULL,
  `mtime` varchar(50) NOT NULL,
  `mdate` varchar(50) NOT NULL,
  `image` varchar(200) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(20) NOT NULL,
  `rdate` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `missing_person`
--

INSERT INTO `missing_person` (`id`, `username`, `name`, `age`, `gender`, `missing_place`, `mtime`, `mdate`, `image`, `status`, `report`, `rdate`) VALUES
(2, 'arun', 'cherry', '23', 'Male', 'trichy', '20:45', '2021-01-20', 'ship2.jpg', 'Action Completed..', '1', 'Jan-06-2021'),
(3, 'arun', 'aaa', '23', 'Male', 'trichy', '11:20', '2021-01-22', 'bg8.jpg', 'Complaint', '0', 'Jan-07-2021');

-- --------------------------------------------------------

--
-- Table structure for table `user_register`
--

CREATE TABLE `user_register` (
  `id` int(11) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `mobile` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(200) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `rdate` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_register`
--

INSERT INTO `user_register` (`id`, `uname`, `mobile`, `email`, `address`, `username`, `password`, `rdate`) VALUES
(1, 'cherry', '986565656565', 'charry@gmail.com', 'trichy', 'arun', '1234', 'Jan-05-2021');
