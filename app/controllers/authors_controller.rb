class AuthorsController < ApplicationController
  
  before_filter :admin_user, only: [:new, :create, :edit, :update, :destroy]

  def index
    @authors = Author.paginate(page: params[:page])
  end

  def show
    @author = Author.find(params[:id])
  end
  
  def new
    @author = Author.new
  end
  
  def create
    @author = Author.new(params[:author])
    if @author.save
      flash[:success] = "Created " + @author.full_name
      redirect_to @author
    else
      render 'new'
    end
  end
  
  def edit
    @author = Author.find(params[:id])
  end
  
  def update
    @author = Author.find(params[:id])
    if @author.update_attributes(params[:author])
      flash[:success] = "Author updated"
      redirect_to @author
    else
      render 'edit'
    end
  end
  
  def destroy
    Author.find(params[:id]).destroy
    flash[:success] = "Author destroyed."
    redirect_to authors_path
  end
end
