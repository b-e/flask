drop table if exists registry;
create table registry (
  id integer primary key autoincrement,
  token text not null,
  endpoint text not null,
  channel text,
  phoneNumber integer not null,
  pid integer
);