USE [PruebaTecnica]
GO
/****** Object:  Schema [tareas]    Script Date: 14/06/2024 2:26:25 p. m. ******/
CREATE SCHEMA [tareas]
GO
/****** Object:  Schema [usuario]    Script Date: 14/06/2024 2:26:25 p. m. ******/
CREATE SCHEMA [usuario]
GO
/****** Object:  Table [tareas].[tarea]    Script Date: 14/06/2024 2:26:25 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [tareas].[tarea](
	[id_tarea] [int] IDENTITY(1,1) NOT NULL,
	[titulo] [varchar](150) NOT NULL,
	[descripcion] [varchar](250) NOT NULL,
	[fecha_creacion] [datetime] NOT NULL,
	[id_usuario] [int] NOT NULL,
 CONSTRAINT [PK_tarea] PRIMARY KEY CLUSTERED 
(
	[id_tarea] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [usuario].[usuario]    Script Date: 14/06/2024 2:26:26 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [usuario].[usuario](
	[id_usuario] [int] IDENTITY(1,1) NOT NULL,
	[usuario] [varchar](100) NOT NULL,
	[contraseña] [varchar](255) NOT NULL,
 CONSTRAINT [PK_usuarios] PRIMARY KEY CLUSTERED 
(
	[id_usuario] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [tareas].[tarea]  WITH CHECK ADD  CONSTRAINT [FK_tarea_usuario] FOREIGN KEY([id_usuario])
REFERENCES [usuario].[usuario] ([id_usuario])
GO
ALTER TABLE [tareas].[tarea] CHECK CONSTRAINT [FK_tarea_usuario]
GO
