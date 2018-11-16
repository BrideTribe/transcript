-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 13, 2018 at 04:31 PM
-- Server version: 10.1.22-MariaDB
-- PHP Version: 7.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `staff`
--

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE `departments` (
  `dept_Id` int(11) NOT NULL,
  `fac_Id` int(11) NOT NULL,
  `department` varchar(200) NOT NULL,
  `HOD` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `departments`
--

INSERT INTO `departments` (`dept_Id`, `fac_Id`, `department`, `HOD`) VALUES
(18408152, 333182711, 'Soil Science', 0),
(31544994, 826904296, 'Fine and Applied Arts', 0),
(42417185, 914430978, 'Preventive Dentistry', 0),
(55329268, 71484570, 'Agricultural Engineering', 0),
(60980131, 826904296, 'Modern Lang. and Trans. Studies', 0),
(81906194, 694191474, 'Ophthalmology', 0),
(91891012, 694191474, 'Surgery', 0),
(119789791, 694191474, 'Anaesthesiology', 0),
(120513916, 470428466, 'Criminal Law', 0),
(124627292, 297143069, 'Mathematics', 0),
(127383446, 357116699, 'Special Education', 0),
(137052397, 470428466, 'Commercial and Industrial Law', 0),
(142425537, 357116699, 'Curriculum & Vocations', 0),
(148000373, 71484570, 'Mechanical Engineering', 0),
(162693056, 694191474, 'Orthopaedic', 0),
(176182866, 297143069, 'Geology', 0),
(178070365, 333182711, 'Forestry & Wildlife Res. MGT.', 0),
(185895534, 357116699, 'Institute of Education', 0),
(185975641, 694191474, 'Pathology', 0),
(206399702, 333182711, 'Faculty Officer', 0),
(217834472, 470428466, 'International Law', 0),
(218261718, 826904296, 'Moden Languages and Translation Studies', 149780273),
(229545158, 914430978, 'Restorative Dentistry', 0),
(231997599, 297143069, 'Computer Science', 0),
(250025010, 694191474, 'Haematology', 0),
(251530796, 826904296, 'History and International Studies', 0),
(259301166, 357116699, 'Library and Information Science', 0),
(272281307, 694191474, 'Paediatrics', 0),
(275416098, 333182711, 'Agricultural Economics', 0),
(275874225, 357116699, 'Environmental Education', 0),
(281186861, 357116699, 'Adult Education', 0),
(296606350, 694191474, 'Medical Microbiology/Parasitology', 0),
(316134143, 982318777, 'Science and Lab. Technology', 0),
(317855646, 357116699, 'Continuing Education/Developmental Studies', 0),
(333331185, 333182711, 'Food Science', 0),
(333843063, 982318777, 'Botany', 0),
(338802765, 694191474, 'Community Medicine', 0),
(351252942, 868339275, 'Radiography', 0),
(363037049, 694191474, 'Psychiatry', 0),
(372075827, 472712947, 'Institute of Oceanography', 0),
(393970676, 816095278, 'Social Work', 0),
(395290362, 71484570, 'Chemical and Petroleum Engineering', 0),
(399445387, 470428466, 'Public Law', 0),
(403264094, 472712947, 'Physical Oceanography', 0),
(409675159, 71484570, 'Civil and Environmental Engineering', 0),
(411835322, 357116699, 'Curriculum and Teaching', 0),
(437582761, 826904296, 'Music', 0),
(440983287, 71484570, 'Computer Engineering', 0),
(445052881, 297143069, 'Statistics', 0),
(449419669, 357116699, 'Agricultural Engineering', 0),
(482925815, 357116699, 'Social Science Education', 0),
(487423492, 702852198, 'Anatomy', 0),
(519675198, 982318777, 'Zoology and Environmental Biology', 0),
(524096861, 472712947, 'Mari Culture and Marine Fisheries Resources', 0),
(526392159, 71484570, 'Electrical and Electronic Engineering', 0),
(530827546, 472712947, 'Biological Oceanography', 0),
(545794405, 470428466, 'Jurisprudence and International Law', 0),
(563299891, 826904296, 'Mass Communication', 476471535),
(566693926, 357116699, 'Human Kinetics and Health Education', 0),
(571205548, 816095278, 'Geography and Environmental Science', 0),
(576630780, 694191474, 'Obstetrics and Gynaecology', 0),
(577365092, 868339275, 'Medical Laboratory Science', 0),
(594882774, 357116699, 'Arts Education', 0),
(609898002, 982318777, 'Microbiology', 0),
(618859242, 694191474, 'Family Medicine', 0),
(622558983, 357116699, 'Educational Foundation', 0),
(623682025, 357116699, 'Science Education', 0),
(629222988, 868339275, 'Nursing Science', 0),
(638642740, 914430978, 'Oral Pathology/Medicine/Diagnosis', 0),
(640075786, 826904296, 'English & Literary Studies', 0),
(642377429, 826904296, 'Religious and Cultural Studies', 0),
(642583261, 702852198, 'Biochemistry', 0),
(716869787, 826904296, 'Philosophy', 0),
(728000226, 297143069, 'Physics', 0),
(740986709, 816095278, 'Economics', 0),
(741255828, 357116699, 'Educational Administration and Planning', 0),
(742697881, 816095278, 'Sociology', 0),
(744520918, 297143069, 'Pure and Applied Chemistry', 0),
(756549392, 547524132, 'Business Management', 0),
(761048722, 547524132, 'Banking and Finance', 0),
(767491028, 868339275, 'Public Health', 0),
(771820854, 333182711, 'Agric. Extension & Rural Sociology', 0),
(800819878, 826904296, 'Theatre and Media Studies', 0),
(807693731, 357116699, 'Vocational Education', 0),
(817519770, 547524132, 'Marketing', 0),
(831177701, 816095278, 'Public Administration', 0),
(832185468, 702852198, 'Pharmacology', 0),
(839300394, 694191474, 'Radiology', 0),
(850816807, 694191474, 'Ortorhinolaryncology', 0),
(858934035, 694191474, 'Chemical Pathology', 0),
(859242304, 333182711, 'Crop Science', 0),
(859509690, 826904296, 'Linguistics and Communication Studies', 0),
(885117007, 702852198, 'Physiology', 0),
(918750026, 914430978, 'Child Dental Health', 0),
(924640439, 914430978, 'Oral and Maxillofacial Surgery', 0),
(929415182, 982318777, 'Genetics and Biotechnology', 0),
(933370203, 547524132, 'Accounting', 0),
(934127238, 816095278, 'Political Science', 0),
(971518273, 470428466, 'Private and Property Law', 0),
(971549684, 357116699, 'Guidance and Counselling', 0),
(981471244, 694191474, 'Internal Medicine', 0),
(999863893, 333182711, 'Animal Science', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `departments`
--
ALTER TABLE `departments`
  ADD PRIMARY KEY (`dept_Id`),
  ADD KEY `fac_Id` (`fac_Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
