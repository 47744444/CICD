FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 6000

ENV ASPNETCORE_URLS=http://+:6000



FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
ARG configuration=Release
WORKDIR /src
COPY ["WebApplication1.csproj", "./"]
RUN dotnet restore "WebApplication1.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "WebApplication1.csproj" -c $configuration -o /app/build

FROM build AS publish
ARG configuration=Release
RUN dotnet publish "WebApplication1.csproj" -c $configuration -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "WebApplication1.dll"]
