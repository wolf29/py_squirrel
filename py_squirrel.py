#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  py_squirrel.py
#  
#  Copyright 2012 Wolf Halton <wolf@sourcefreedom.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

/* To Do:
	The basic plan is to take an sql dump of a postgresql database cluster and create a file for each table, reading the file for markers to show when the databases, schemas, and tables start and stop.
	My current solution uses the marker text:
		Cluster_name.dmp mkdir cluster_name:
			SET command_name >> $clustername/set_commands.set
			CREATE ROLE role_name >> $clustername/roles.role
			ALTER ROLE role_name  >> $clustername/roles.role
			CREATE DATABASE database_name: mkdir $DATABASE:
				ALTER DATABASE database_name >> $cluster_name/$DATABASE/$database_name.comment 
				COMMENT ON DATABASE database_name >> $DATABASE/$database_name.comment
				PROCEDURAL LANGUAGE (anything related to the procedural languages in the db) >> $DATABASE/database_name.comment
				CREATE SCHEMA schema_name: mkdir $DATABASE/SCHEMA:
					ALTER SCHEMA schema_name >> $DATABASE/$SCHEMA/schema_name.comment
					COMMENT ON SCHEMA schema_name >> $DATABASE/$SCHEMA/schema_name.comment
					CREATE TYPE $SCHEMA.type_name (the detail of this is found in an sql comment '-- Name: type_name; Type: TYPE; Chema schema_name; Owner: owner;') >> $DATABASE/$SCHEMA/typename.type
					ALTER TYPE $SCHEMA.type_name >> $DATABASE/$SCHEMA/typename.type
					CREATE FUNCTION $SCHEMA.function_name >> $DATABASE/$SCHEMA/function_name.func
					ALTER FUNCTION $SCHEMA.function_name >> $DATABASE/$SCHEMA/function_name.func
					COMMENT on FUNCTION $SCHEMA.function_name >> $DATABASE/$SCHEMA/function_name.func
					CREATE TABLE $SCHEMA.tablename >> $DATABASE/$SCHEMA/table_name.table
					ALTER TABLE $SCHEMA.tablename >> $DATABASE/$SCHEMA/table_name.comments
					
*/				

def main():
	
	return 0

if __name__ == '__main__':
	main()

