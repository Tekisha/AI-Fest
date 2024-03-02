import * as React from "react";

const Card = ({ className, ...props }) => <div className={"rounded-xl border bg-card text-card-foreground shadow"} {...props} />;

const CardHeader = ({ className, ...props }) => <div className={"flex flex-col space-y-1.5 pb-6 font-semibold"} {...props} />;

// eslint-disable-next-line
const CardTitle = ({ className, ...props }) => <h3 className={"font-semibold leading-none tracking-tight"} {...props} />;

const CardDescription = ({ className, ...props }) => <p className={"text-sm text-muted-foreground text-justify"} {...props} />;

const CardContent = ({ className, ...props }) => <div className={"p-6 pt-0"} {...props} />;

const CardFooter = ({ className, ...props }) => <div className={"flex items-center p-6 pt-0"} {...props} />;

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent };
