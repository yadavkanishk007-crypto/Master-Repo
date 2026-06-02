\documentclass[10pt,a4paper,sans]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=0.5in]{geometry}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{bold-extra}

% Color Definitions
\definecolor{primary}{HTML}{1A365D}   % Deep Navy
\definecolor{secondary}{HTML}{2B6CB0} % Slate Blue
\definecolor{textdark}{HTML}{2D3748}  % Dark Charcoal
\definecolor{accent}{HTML}{4A5568}    % Cool Grey

% Font Configurations
\renewcommand{\familydefault}{\sfdefault}

% Hyperref Styling
\hypersetup{
    colorlinks=true,
    linkcolor=secondary,
    urlcolor=secondary,
    pdftitle={Kanishk Yadav - Curriculum Vitae},
    pdfauthor={Kanishk Yadav}
}

% Section Title Styling
\titleformat{\section}
  {\color{primary}\normalfont\large\bfseries\uppercase}
  {}{0em}
  {}[\titlerule]
\titlespacing*{\section}{0pt}{10pt}{6pt}

\titleformat{\subsection}
  {\color{secondary}\normalfont\subsectionfont\bfseries}
  {}{0em}
  {}
\titlespacing*{\subsection}{0pt}{6pt}{3pt}

% Custom commands for styling
\newcommand{\subsectionfont}{\fontsize{11}{13}\selectfont}
\newcommand{\projecttitle}[1]{{\noindent\textbf{\color{primary}#1}}}
\newcommand{\challengeitem}[2]{\item \textbf{#1:} #2}

% Setup itemize lists
\setlist[itemize]{leftmargin=12pt, topsep=2pt, itemsep=2pt, parsep=1pt}

\begin{document}
\thispagestyle{empty}

%----------------------------------------------------------------------------------------
%   HEADER SECTION
%----------------------------------------------------------------------------------------
\begin{center}
    {\Huge \textbf{\color{primary}KANISHK YADAV}} \\[\baselineskip]
    {\large \textbf{\color{accent}System Architect \& AI/ML Engineer}} \\[\baselineskip]
    \href{mailto:kanishkyadav@dinedeal.in}{kanishkyadav@dinedeal.in} \,$\cdot$\, 
    +91 9336239858 \,$\cdot$\, 
    \href{https://www.linkedin.com/in/kanishk-yadav-382807257}{linkedin.com/in/kanishk-yadav-382807257} \,$\cdot$\, 
    \href{https://github.com/yadavkanishk007-crypto}{github.com/yadavkanishk007-crypto}
\end{center}

%----------------------------------------------------------------------------------------
%   CORE TECHNICAL EXPERTISE
%----------------------------------------------------------------------------------------
\section{Core Technical Expertise}
\begin{itemize}
    \item \textbf{Deep Learning \& Time-Series:} Hybrid ARIMA-LSTM Modeling, Predictive Analytics, Autoregressive Weight Matrices, Fourier Seasonal Projections
    \item \textbf{Infrastructure \& Cloud:} Google Cloud Platform (GCP), Cloud Run, Serverless Functions, Docker, Microservices Architecture
    \item \textbf{Computer Vision \& Streaming:} YOLOv8 (Ultralytics), ONNX Runtime, Real-Time WebSockets, RTSP/HLS Stream Ingestion
    \item \textbf{Full-Stack \& Databases:} Next.js/React, Flutter/Dart, Supabase (PostgreSQL with RLS), SQLite (WAL Mode), MySQL
\end{itemize}

%----------------------------------------------------------------------------------------
%   EDUCATION
%----------------------------------------------------------------------------------------
\section{Education}
\noindent \textbf{Lakshmi Narain College of Technology}, Bhopal \hfill Expected Graduation: July 2028 \\
\textit{Bachelor of Technology (B.Tech.) in Engineering} \\
\textit{Professional Affiliation:} Student Member, IEEE (Active since March 2026)

%----------------------------------------------------------------------------------------
%   PROFESSIONAL \& VENTURE EXPERIENCE
%----------------------------------------------------------------------------------------
\section{Professional \& Venture Experience}
\noindent \textbf{\large DineDeal Solutions LLP} \hfill \textbf{April 2026 -- Present} \\
\textit{Founder, CTO, \& System Architect}
\begin{itemize}
    \item Architected the core system layout using a \textbf{Collaborative Infrastructure} model, scaling the platform's foundation to meet strict state-level and Startup India government grant criteria.
    \item Designed the end-to-end data schema and transactional mechanics to handle high-concurrency resource sharing without centralized performance bottlenecks.
    \item \textbf{Strategic Leadership:} Managed legal incorporation processes with the Ministry of Corporate Affairs (MCA) and established cross-functional departmental workflows between creative, operations, and development.
\end{itemize}

%----------------------------------------------------------------------------------------
%   CORE PROJECT ECOSYSTEM \& RESEARCH WORKS
%----------------------------------------------------------------------------------------
\section{Core Project Ecosystem \& Research Works}

\subsection{AuraGrid \& WebCommand (Smart Grid Telemetry Ecosystem) \normalfont\small\hfill \textbf{Team Lead | Final Stage}}
\projecttitle{AuraGrid Engine:} \href{https://github.com/yadavkanishk007-crypto/AURAGRID}{github.com/yadavkanishk007-crypto/AURAGRID} \,$\cdot$\, \textbf{Live API:} \href{https://auragrid-backend-689922962048.asia-south1.run.app}{GCP Cloud Run Endpoint} \\
\projecttitle{WebCommand Center:} \href{https://github.com/yadavkanishk007-crypto/WEBCOMMAND}{github.com/yadavkanishk007-crypto/WEBCOMMAND} \,$\cdot$\, \textbf{Live Hub:} \href{https://webcommand-center-689922962048.asia-south1.run.app}{GCP WebCommand Live}
\begin{itemize}
    \item Solely designed and engineered an advanced telemetry ingestion, forecasting, and simulation platform to prevent cascading outages across multi-tier Indian municipal grids, calibrated using the real-world \textbf{Bengaluru BESCOM Network topology}.
    \item Integrated deep learning LSTM models (12-lag autoregressive weight matrices) with ARIMA models (Fourier seasonal cycle projections) to execute a unified mathematical load prediction pipeline: $L_t = 0.6 \cdot LSTM + 0.4 \cdot ARIMA$.
    \item \textbf{Architectural Challenges Conquered:}
    \begin{itemize}
        \challengeitem{The Challenge}{Managing real-time data ingestion of thousands of grid telemetry points per second while synchronizing a persistent background daemon (ticking every 2 seconds) across an Android client, web dashboard, and Supabase without generating severe database lock or data race conditions.}
        \challengeitem{The Solution}{Developed a decoupled microservices communication layer utilizing an in-memory telemetry store to handle real-time states asynchronously. Implemented a Compartment Mass-Balance Filter that handles boundary violations and isolates failing nodes over a 12-to-24 hour horizon before securely flushing structural logs down to the persistent database layer via Row Level Security (RLS) policies.}
    \end{itemize}
\end{itemize}

\subsection{SwasthAI Ecosystem (Cloud Brain \& Command Centre) \normalfont\small\hfill \textbf{Lead Developer}}
\projecttitle{Cloud Brain:} \href{https://github.com/yadavkanishk007-crypto/SwasthAI}{github.com/yadavkanishk007-crypto/SwasthAI} \,$\cdot$\, \projecttitle{Command Centre:} \href{https://github.com/yadavkanishk007-crypto/Command_Centre}{github.com/yadavkanishk007-crypto/Command_Centre} \,$\cdot$\, \textbf{Live UI:} \href{https://command-centre-lilac.vercel.app/}{command-centre-lilac.vercel.app}
\begin{itemize}
    \item Engineered an autonomous smart-city healthcare intelligence system pairing a heavy predictive machine learning backend with an intuitive Next.js, React, and Mapbox-driven operational UI dashboard layer.
    \item Fused predictive ARIMA models with a deep LSTM Neural Network trained on \textbf{766,000+ synthetic patient records} via cloud GPUs to forecast regional patient inflows, localize load-balancing, and detect pandemic-level anomalies.
    \item \textbf{Architectural Challenges Conquered:}
    \begin{itemize}
        \challengeitem{The Challenge}{Decoupling resource-heavy ML forecasting cycles and multi-hospital overload simulation threads from the live dashboard frontend to avoid UI freezing and API latency spikes.}
        \challengeitem{The Solution}{Implemented an asynchronous backend infrastructure leveraging an automatic database failover system (gracefully defaulting from a local MySQL instance to an optimized thread-local SQLite setup in WAL mode). Handled massive payload extractions within 5--10 seconds on standalone client runtimes using memory-isolated background threads.}
    \end{itemize}
\end{itemize}

\subsection{GOD'S EYE (Urban Intelligence System) \normalfont\small\hfill \textbf{Pipeline Engineer}}
\projecttitle{Repository:} \href{https://github.com/yadavkanishk007-crypto/GOD-s-EYE}{github.com/yadavkanishk007-crypto/GOD-s-EYE}
\begin{itemize}
    \item Engineered a high-performance, proprietary Urban Intelligence and Surveillance system designed to ingest heterogeneous camera feeds (RTSP, HTTP, HLS) for real-time crowd analytics, tracking, and incident detection.
    \item \textbf{Architectural Challenges Conquered:}
    \begin{itemize}
        \challengeitem{The Challenge}{Overcoming Python’s Global Interpreter Lock (GIL) and reducing massive RAM consumption when running heavy YOLOv8 computer vision models simultaneously across multiple active video streams.}
        \challengeitem{The Solution}{Architected a strict \textbf{Multiprocessing Architecture} where each camera stream operates inside its own isolated OS process. Configured an intelligent Inter-Process Communication (IPC) pipeline passing heavily compressed JPEG queues instead of raw video frames, keeping memory consumption low, and built an auto-healing connection logic with adaptive quality degradation for low-bandwidth environments.}
    \end{itemize}
\end{itemize}

\subsection{SwasthPHC (Frontline Public Health Platform) \normalfont\small\hfill \textbf{Systems Engineer}}
\projecttitle{Repository:} \href{https://github.com/yadavkanishk007-crypto/SwasthPHC}{github.com/yadavkanishk007-crypto/SwasthPHC}
\begin{itemize}
    \item Developed a native multi-platform Flutter client mapping field medical personnel to specific regional jurisdictions for grassroots epidemiological tracking, inventory management, and incident reporting.
    \item \textbf{Architectural Challenges Conquered:}
    \begin{itemize}
        \challengeitem{The Challenge}{Ensuring bulletproof data ingestion and synchronizations for Primary Health Centre (PHC) staff operating in remote rural environments with highly volatile or absent internet connectivity.}
        \challengeitem{The Solution}{Designed a strict offline-first data caching paradigm that intercepts state transactions locally. The architecture utilizes dynamic payload synchronization to reconcile offline-logged epidemiological metrics seamlessly with Supabase PostgreSQL servers once an active internet connection is verified.}
    \end{itemize}
\end{itemize}

%----------------------------------------------------------------------------------------
%   PUBLICATIONS \& DOMAIN MONITORING
%----------------------------------------------------------------------------------------
\section{Publications \& Domain Monitoring}
\begin{itemize}
    \item \textbf{Research Paper:} \textit{"SwasthAI: A Hybrid ARIMA-LSTM Framework for Predictive Hospital Administration"} -- Submitted to ICACECS 2026 (Under Review / Presentation Track).
    \item \textbf{Research Focus Areas:} Active tracker of Scientific Machine Learning (SciML), specifically monitoring advancements in Physics-Informed Neural Networks (PINNs) and Ordinary Differential Equation (ODE) solvers under arXiv section cs.LG.
\end{itemize}

%----------------------------------------------------------------------------------------
%   HACKATHONS \& ENGINEERING ACHIEVEMENTS
%----------------------------------------------------------------------------------------
\section{Hackathons \& Engineering Achievements}
\begin{itemize}
    \item \textbf{Team Lead | Pashmina Bytes:} Competed in \textbf{MumbaiHacks 2025}, driving rapid prototyping of high-stress AI/ML software models.
    \item \textbf{GCP Production Architect:} Configured and managed enterprise-grade container pipelines running live production systems in the \texttt{asia-south1} region under strict API access boundaries.
\end{itemize}

\end{document}
