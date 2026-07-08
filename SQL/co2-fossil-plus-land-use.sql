SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Landing].[co2-fossil-plus-land-use](
	[Entity] [varchar](8000) NULL,
	[Code] [varchar](8000) NULL,
	[Year] [varchar](8000) NULL,
	[Total (fossil fuels and land-use change)] [varchar](8000) NULL,
	[Land-use change] [varchar](8000) NULL,
	[Fossil fuels] [varchar](8000) NULL
) ON [PRIMARY]
GO
CREATE CLUSTERED COLUMNSTORE INDEX [ClusteredIndex] ON [Landing].[co2-fossil-plus-land-use] WITH (DROP_EXISTING = OFF, COMPRESSION_DELAY = 0) ON [PRIMARY]
GO
