SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Landing].[cumulative-co2-emissions-region](
	[Entity] [varchar](8000) NULL,
	[Code] [varchar](8000) NULL,
	[Year] [varchar](8000) NULL,
	[Cumulative CO₂ emissions] [varchar](8000) NULL
) ON [PRIMARY]
GO
CREATE CLUSTERED COLUMNSTORE INDEX [ClusteredIndex] ON [Landing].[cumulative-co2-emissions-region] WITH (DROP_EXISTING = OFF, COMPRESSION_DELAY = 0) ON [PRIMARY]
GO
