SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Landing].[co2-emissions-per-capita](
	[Entity] [varchar](8000) NULL,
	[Code] [varchar](8000) NULL,
	[Year] [varchar](8000) NULL,
	[CO₂ emissions per capita] [varchar](8000) NULL
) ON [PRIMARY]
GO
CREATE CLUSTERED COLUMNSTORE INDEX [ClusteredIndex] ON [Landing].[co2-emissions-per-capita] WITH (DROP_EXISTING = OFF, COMPRESSION_DELAY = 0) ON [PRIMARY]
GO
